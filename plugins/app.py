from client import app
from swibots import *
from database.ia_filterdb import get_search_results, get_file_details, getMovie


def humanbytes(size):
    if not size:
        return "0 B"
    for unit in ["", "K", "M", "G", "T"]:
        if size < 1024:
            break
        size /= 1024
    if isinstance(size, int):
        size = f"{size}{unit}B"
    elif isinstance(size, float):
        size = f"{size:.2f}{unit}B"
    return size

@app.on_callback_query(regexp("vfile"))
async def onHome(ctx: BotContext[CallbackQueryEvent]):
    fileId = ctx.event.callback_data.split("|")[-1]
    details = await get_file_details(int(fileId))
    if not details:
        await ctx.event.answer("File not found", show_alert=True)
        return
    details = details[0]
    iData = {}
    if details.imdb_id:
        iData = await getMovie(details.imdb_id,
                               type="tv" if details.tv_show else "movie")
    #       print(iData)
    #    print(details)
    comps = []
    if details.description.endswith((".mkv", ".mp4", ".webm")):
        comps.append(
            VideoPlayer(
                details.file_url,
                title=details.movie_name or details.description or details.file_name,
            )
        )
    elif details.description.endswith((".jpeg", ".jpg", ".png")):
        comps.append(Image(url=details.file_url))
    # else:
    #     comps.append(Text(details.movie_name or details.description, TextSize.SMALL))
    if iD := iData.get("overview"):
        comps.append(Text(iD))
    if iD := iData.get("vote_average"):
        comps.append(Text(f"*Rating:* {iD} ⭐"))
    if iD:= details.file_size:
        comps.append(Text(f"*File Size:* {humanbytes(iD)}"))
    if iD := iData.get("release_date"):
        comps.append(Text(f"*Released on:* {iD}"))
    if iD := iData.get("status"):
        comps.append(Text(f"*Status:* {iD}"))
    comps.append(Text(f"*File Name:* {details.description or details.file_name}"))
    comps.append(
        ButtonGroup(
            [
                Button("Get File", callback_data=f"blk_{fileId}"),
                ShareButton(
                    "Share file",
                    share_text=f"https://iswitch.click/{ctx.user.user_name}?start={fileId}",
                ),
            ]
        ),
    )
    await ctx.event.answer(
        callback=AppPage(
            components=comps,
        ),
        new_page=True,
    )


async def makeListTiles(query="", max=25):
    results, _, __ = await get_search_results(query, max_results=max)
    gV = []
    for file in results:
        gV.append(
            ListTile(
                file.movie_name or file.description or file.file_name,
                title_extra=f"Episode {file.episode_id}" if file.tv_show else None,
                thumb=(
                    file.thumbnail
                    if file.thumbnail
                    else (
                        file.file_url
                        if file.description.endswith((".jpg", ".png", ".jpeg"))
                        else "https://media.istockphoto.com/id/1147544810/vector/no-thumbnail-image-vector-graphic.jpg?s=612x612&w=0&k=20&c=2-ScbybM7bUYw-nptQXyKKjwRHKQZ9fEIwoWmZG9Zyg="
                    )
                ),
                description=f"File Size: {humanbytes(file.file_size)}",
                callback_data=f"vfile|{file.file_id}",
            )
        )
    return gV

def splitList(lis, part):
    nList = []
    while lis:
        nList.append(lis[:part])
        lis = lis[part:]
    return nList

@app.on_callback_query(regexp("srch"))
async def onHome(ctx: BotContext[CallbackQueryEvent]):
    comps = [SearchBar("Search files", callback_data="srch")]
    index =  1
    query = ctx.event.details.search_query
    if "|" in ctx.event.callback_data:
        query, index = ctx.event.callback_data.split("|")[1:]
        index = int(index)

    if query:
        gV = await makeListTiles(query, 80)
        if gV:
            BOXES = splitList(gV, 10)
            try:
                gV = BOXES[index - 1]
            except:
                gV = gV[0]
        if gV:
            comps.append(Text(f"*Results for {query}*", TextSize.SMALL))
            comps.append(ListView(options=gV, view_type=ListViewType.LARGE))
            bts = []
            if index > 1:
                bts.append(Button("Back", callback_data=f"srch|{query}|{index-1}"))
            if index < len(BOXES):
                bts.append(Button("Next", callback_data=f"srch|{query}|{index+1}"))
            comps.append(
                ButtonGroup(bts)
            )
        else:
            comps.append(Text(f"No results found for {query}!", TextSize.SMALL))
    await ctx.event.answer(
        callback=AppPage(components=comps), new_page=not query
    )


@app.on_callback_query(regexp("Home"))
async def onHome(ctx: BotContext[CallbackQueryEvent]):
    comps = [
        SearchHolder("Search files..", callback_data="srch")
    ]
    gv = await makeListTiles(max=50)
    if gv:
        comps.append(
            Text("Recently Uploaded", TextSize.SMALL)
        )
        comps.append(
            ListView(
                gv, ListViewType.LARGE
            )
        )
    await ctx.event.answer(
        callback=AppPage(
            components=comps
        )
    )

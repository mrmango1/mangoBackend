from typing import List
import httpx
from bs4 import BeautifulSoup


def getMangas(
    num: int,
    webPage: str = "mangacrab.com",
) -> dict:
    url = f"https://{webPage}"
    reqUrl = f"{url}/wp-admin/admin-ajax.php"
    print(reqUrl)
    headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = f"action=madara_load_more&template=madara-core/content/content-archive&vars[orderby]=meta_value_num&vars[posts_per_page]={num}&vars[post_type]=wp-manga&vars[meta_key]=_latest_update"
    response = httpx.post(reqUrl, data=payload, headers=headersList)
    soup_data = BeautifulSoup(response.text, "html.parser")
    mangas = soup_data.find_all("div", class_="manga")
    mangaList = filterData(mangas)
    return {"website": url, "numberOfManga": len(mangaList), "mangas": mangaList}


def filterData(html: BeautifulSoup) -> List:
    dataList = []
    try:
        for manga in html:
            searchAll = manga.findAll("a")
            mangaUrl = searchAll[0]["href"]
            mangaImg = searchAll[0].find("img")["src"]
            mangaTitle = searchAll[0]["title"]
            mangaLinkLastChapter = searchAll[2]["href"]
            mangaLastChapter = searchAll[2].string.strip()
            mangaJson = {
                "url": mangaUrl,
                "img": mangaImg,
                "title": mangaTitle,
                "linkLastChapter": mangaLinkLastChapter,
                "lastChapter": mangaLastChapter,
            }
            dataList.append(mangaJson)
    except:
        for manga in html:
            searchAll = manga.findAll("a")
            mangaUrl = searchAll[1]["href"]
            mangaImg = searchAll[1].find("img")["src"]
            mangaTitle = searchAll[1]["title"]
            mangaLinkLastChapter = searchAll[2]["href"]
            mangaLastChapter = searchAll[2].string.strip()
            mangaJson = {
                "url": mangaUrl,
                "img": mangaImg,
                "title": mangaTitle,
                "linkLastChapter": mangaLinkLastChapter,
                "lastChapter": mangaLastChapter,
            }
            dataList.append(mangaJson)
    return dataList


def getImages(reqUrl: str):
    headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)"
    }
    response = httpx.get(reqUrl, headers=headersList)
    soup_data = BeautifulSoup(response.text, "html.parser")
    imageContainer = soup_data.find("div", class_="reading-content")
    images = imageContainer.find_all('img')
    mangaImages = []
    for image in images:
        mangaImages.append(image["src"].strip())
    print(mangaImages)

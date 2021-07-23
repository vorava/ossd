#!/usr/bin/env python
# Licence: MIT (free commercial use)
# Author: Vojtech Orava
# Link: https://github.com/vorava/ossd

import requests
import time

# default link:
# https://www.opensubtitles.org/en/search/sublanguageid-eng/moviename-NAME

# returns most downloaded subtitles text, params: chromedriver, name of movie
# if error occurs returns " " and prints error code
def get_subtitles(driver, movieName, year = ""):
    driver.get("https://www.opensubtitles.org/en/search/sublanguageid-eng/moviename-" + movieName + " " + year)

    # finding most downloaded subtitles
    try:
        tab = driver.find_element_by_id("search_results")
        trs = tab.find_elements_by_tag_name("tr")
    except Exception:
        print("ERR_TAB")
        return " "

    # selecting most downloaded subtitles from subtitles list
    mostDownloaded = 0
    id = None
    for tr in trs:
        try:
            n = tr.find_elements_by_tag_name("td")[4].find_element_by_tag_name("a").text
            n = int(n.strip()[:-1])
            if n > mostDownloaded:
                mostDownloaded = n
                id = tr
        except IndexError:
            pass

    # loading most downloaded subtitles page
    subtitlesId = id.get_attribute("id").replace("main", "").replace("name", "")

    driver.get("https://www.opensubtitles.org/en/subtitles/" + subtitlesId)
    try:
        subtitlesFile = driver.find_element_by_id("moviehash").find_element_by_tag_name("a") \
            .get_attribute("href")
    except Exception:
        print("ERR_SUBT")
        return " "

    # downloading subtitles text
    response = requests.get(subtitlesFile)
    while response.status_code == 429:
        time.sleep(60)
        response = requests.get(subtitlesFile)
    text = response.text  # subtitles text
    return text

# parses script lines from default format into one line only text format
# skips ads on the script start
def parse_subtitles(lines):
    output = []
    lines.replace("\r", "")
    lineArr = lines.split("\n")

    for i in range(len(lineArr)):
        try:  # check if line is only number
            int(lineArr[i])
            i += 2  # skip 2 lines to get to the text
            if "Support us and become VIP member" not in lineArr[i] and "Advertise" not in lineArr[i]\
                    and "www.OpenSubtitles.org" not in lineArr[i]:
                output.append(lineArr[i].replace("\r", ""))
            # write all text line till there is white line
            i += 1
            while lineArr[i].strip() != "" and i < len(lineArr):
                if "Support us and become VIP member" not in lineArr[i] and "Advertise" not in lineArr[i]\
                        and "www.OpenSubtitles.org" not in lineArr[i]:
                    output.append(lineArr[i].replace("\r", ""))
                i += 1

        except ValueError:
            continue

        except IndexError:
            break

    return " ".join(output)

#!/usr/bin/env python
# Licence: MIT (free commercial use)
# Author: Vojtech Orava

from selenium import webdriver
import requests

# default link:
# https://www.opensubtitles.org/en/search/sublanguageid-eng/moviename-NAME

# returns most downloaded subtitles text, params: chromedriver, name of movie
# if error occurs returns " " and print error code
def get_subtitles(driver, movieName):
    driver.get("https://www.opensubtitles.org/en/search/sublanguageid-eng/moviename-" + movieName)

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
    text = response.text  # subtitles text
    return text

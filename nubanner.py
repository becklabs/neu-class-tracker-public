import requests


def makeRequest(subject, courseNumber):
  url = "https://nubanner.neu.edu/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_subjectcoursecombo={subject}{couseNumber}&txt_term=202210&pageOffset=0&pageMaxSize=10&sortColumn=subjectDescription&sortDirection=asc"

  headers = {
      'Connection': 'close',
      'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
      'Accept': 'application/json, text/javascript, */*; q=0.01',
      'X-Synchronizer-Token': '96a84046-0dc8-4744-8e24-931d5b4f2cf9',
      'X-Requested-With': 'XMLHttpRequest',
      'sec-ch-ua-mobile': '?0',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
      'Sec-Fetch-Site': 'same-origin',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Dest': 'empty',
      'Referer': 'https://nubanner.neu.edu/StudentRegistrationSsb/ssb/courseSearch/courseSearch',
      'Accept-Language': 'en-US,en;q=0.9',
      'Cookie': 'JSESSIONID=57FE8F812FC89BF650F71DD428973DC7; nubanner-cookie=2334073243.36895.0000; _ga=GA1.2.981078370.1629321202; _gid=GA1.2.955840964.1629321202; _gat_Ellucian=1; JSESSIONID=10653135818C21523D3F07ABD3339F6D; nubanner-cookie=2334073243.36895.0000'
  }

  response = requests.request("GET", url, headers=headers, data={})
  return response.json()


def parseResponse(response):
  data_dict = {}
  for result in response['data']:
    data_dict[result['courseReferenceNumber']] = result['seatsAvailable'] != 0
  return data_dict


def getClassData(subject, courseNumber):
  return parseResponse(makeRequest(subject, courseNumber))

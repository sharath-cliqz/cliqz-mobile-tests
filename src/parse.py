from ast import literal_eval
import xlwt
import datetime


def dict_zip(*dicts):
    return {k: [d[k] for d in dicts] for k in dicts[0].keys()}


def read_reports():
    with open("reports/Safari.txt", "r") as fp:
        safari = literal_eval(fp.read())
    with open("reports/Cliqz.txt", "r") as fp1:
        cliqz = literal_eval(fp1.read())
    return dict_zip(safari, cliqz)


def time_diff(time1, time2):
    """
    Pass String values of 2 datetime.timedelta
    :param time1: STRING:   converted to datetime.timedelta
    :param time2: STRING:   converted to datetime.timedelta
    :return: Returns time1 - time2
    """
    startOfTime = datetime.datetime.strptime("00:00:00.000000", "%H:%M:%S.%f")
    time1 = datetime.datetime.strptime(time1, "%H:%M:%S.%f") - startOfTime
    time2 = datetime.datetime.strptime(time2, "%H:%M:%S.%f") - startOfTime
    if time1 > time2:
        diff = time1 - time2
        return "- {}.{}".format(diff.seconds, diff.microseconds)
    else:
        diff = time2 - time1
        return "+ {}.{}".format(diff.seconds, diff.microseconds)


def write_to_file():
    result = read_reports()
    with open("reports/performance.txt", "w") as fp:
        for webpage in result:
            webpageResultList = result[webpage]
            if "Safari" in webpageResultList[0]:
                safariTimes = webpageResultList[0]["Safari"]
                cliqzTimes = webpageResultList[1]["Cliqz"]
            else:
                safariTimes = webpageResultList[1]["Safari"]
                cliqzTimes = webpageResultList[0]["Cliqz"]
            safariAvg = safariTimes.pop("avg")
            cliqzAvg = cliqzTimes.pop("avg")
            diff = time_diff(safariAvg, cliqzAvg)
            safariResult = "{} - {} {}   [{}]".format(
                "Safari", safariAvg, "".rjust(len(diff)+2, " "), ", ".join(safariTimes.values()))
            cliqzResult = "{}  - {} ({})   [{}]".format(
                "Lumen", cliqzAvg, diff, ", ".join(cliqzTimes.values()))
            jointResult = "{}\n{}\n{}\n\n".format(webpage, safariResult, cliqzResult)
            print(jointResult)
            fp.write(jointResult)


def write_to_excel():
    result = read_reports()
    book = xlwt.Workbook()
    sh_summary = book.add_sheet("summary")
    sh_safari = book.add_sheet("safari")
    sh_cliqz = book.add_sheet("lumen")
    sh_safari.write(0, 0, "Webpage")
    sh_cliqz.write(0, 0, "Webpage")
    sh_summary.write(0, 0, "Webpage")
    sh_summary.write(0, 1, "Safari")
    sh_summary.write(0, 2, "Lumen")
    sh_summary.write(0, 3, "Diff")
    sh_summary.write(0, 4, "(w.r.t Lumen; Negative means Lumen is faster)")
    sh_summary.write(1, 4, "(ALL TIMES ARE IN SECONDS !!)")
    avgCol = 0
    col = 1
    for value in result.values()[0][0].values()[0].keys():
        if value.lower() == "avg":
            avgCol = col
        sh_safari.write(0, col, "Test Run {}".format(col) if value.lower() != "avg" else "AVG")
        sh_cliqz.write(0, col, "Test Run {}".format(col) if value.lower() != "avg" else "AVG")
        col += 1
    row = 1
    for webpage in result:
        sh_summary.write(row, 0, webpage)
        sh_cliqz.write(row, 0, webpage)
        sh_safari.write(row, 0, webpage)
        webpageResultList = result[webpage]
        if "Safari" in webpageResultList[0]:
            safariResults = webpageResultList[0]["Safari"]
            cliqzResults = webpageResultList[1]["Cliqz"]
        else:
            safariResults = webpageResultList[1]["Safari"]
            cliqzResults = webpageResultList[0]["Cliqz"]
        col = 1
        for key in safariResults:
            if key == "avg":
                sh_safari.write(row, avgCol, safariResults[key])
                sh_summary.write(row, 1, safariResults[key])
            else:
                sh_safari.write(row, col, safariResults[key])
                col += 1
        col = 1
        for key in cliqzResults:
            if key == "avg":
                sh_cliqz.write(row, avgCol, cliqzResults[key])
                sh_summary.write(row, 2, cliqzResults[key])
            else:
                sh_cliqz.write(row, col, cliqzResults[key])
                col += 1
        sh_summary.write(row, 3, time_diff(safariResults["avg"], cliqzResults["avg"]))
        row += 1
    book.save('reports/Performance.xls')


if __name__ == "__main__":
    write_to_file()
    write_to_excel()

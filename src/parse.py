from ast import literal_eval


with open("Safari.txt", "r") as fp:
    safari = literal_eval(fp.read())

with open("Cliqz.txt", "r") as fp1:
    cliqz = literal_eval(fp1.read())

result = {key: (value1, value2) for key, value1, value2 in zip(safari.keys(), safari.values(), cliqz.values())}

with open("performance.txt", "w") as fp:
    for webpage in result:
        list = result[webpage]
        jointResult = "{}\n{} - {}\n{} - {}\n\n".format(webpage,
                                                list[0].keys()[0], list[0].values()[0],
                                                list[1].keys()[0], list[1].values()[0])
        print(jointResult)
        fp.write(jointResult)
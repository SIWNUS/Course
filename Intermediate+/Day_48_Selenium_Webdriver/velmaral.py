with open("vel_maral.txt", 'r') as fp:
    contents = fp.readlines()

velmaral_li = []
for content in contents:
    content = content.strip("\n")
    velmaral_li.append(content)

repe_lines = [line.replace("( … இந்த அடியை முதலில் 20 முறை ஓதவும் … )", "") for line in velmaral_li[29:33]]
ch_text = ''
for item in repe_lines:
    item += "\n"
    ch_text += item

for line in velmaral_li:
    line = line.replace("( … திரு … )", f"\n\n{ch_text}")
    with open("Final.txt", 'a') as fp:
        fp.write(line)
        fp.write("\n")


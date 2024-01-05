#! /bin/python3

import csv


# Reading the template files from the disk
htmlTemplateFile        = open('templates/template.html', 'r')
cssTemplateFile         = open('templates/template.css', 'r')
entryTemplateFile       = open('templates/entryTemplate.html', 'r')
blankTemplateFile       = open('templates/blankTemplate.html', 'r')
categoryTemplateFile    = open('templates/entryTemplate.css', 'r')

htmlTemplate        = htmlTemplateFile.read()
cssTemplate         = cssTemplateFile.read()
entryTemplate       = entryTemplateFile.read()
blankTemplate       = blankTemplateFile.read()
categoryTemplate    = categoryTemplateFile.read()

htmlTemplateFile.close()
cssTemplateFile.close()
entryTemplateFile.close()
blankTemplateFile.close()
categoryTemplateFile.close()

index = 1
count = 1


# Reading the content from the file on disk & inserting it into the template
with open('content.csv', 'r') as file:
    content = csv.reader(file)
    for entry in content:
        if len(entry) == 0:
            continue
        elif entry[0] == 'blank':
            htmlTemplate = htmlTemplate.format(entry=blankTemplate, styles='{styles}')
        else:
            htmlTemplate = htmlTemplate.format(entry=entryTemplate.format(
            url			= 'https://' + entry[1].lstrip(),
            category	= entry[2].lstrip(),
            index		= index,
            short		= entry[0][0:2].title(),
            name		= entry[0].title(),
            entry 		= '{entry}'
            )[:-1], styles = '{styles}')
            index += 1
        count += 1

with open('categories.csv', 'r') as file:
    content = csv.reader(file)
    for entry in content:
        if len(entry) == 0:
            continue
        else:
            cssTemplate = cssTemplate.replace('$entry$', categoryTemplate.replace('$category$', entry[0]).replace('$color$', entry[1].lstrip()))


# Setting the correct values in the css
width = round(count / 5)
formWidth = 152 * width + 19 * (width - 1)

cssTemplate = cssTemplate.replace('$width$', ('auto ' * width)[:-1])
cssTemplate = cssTemplate.replace('$formWidth$', str(formWidth) + 'px')
cssTemplate = cssTemplate.replace('$inputWidth$', str(formWidth - 56) + 'px')
cssTemplate = cssTemplate.replace('$entry$', '')


# Cleaning the html template
htmlTemplate = htmlTemplate.format(entry='', styles=cssTemplate)

htmlFile	= open('home.html', 'w')
htmlFile.write(htmlTemplate)
htmlFile.close()

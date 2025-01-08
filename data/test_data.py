FILES_W_TEXT_CONTENT = {
    'text-test1.txt': {'content': 'This text file is created for text purposes. Please ignore.'},
    'text-test2.txt': {'content': 'This second text file is created for text purposes. Please ignore.'},
}
FILES_W_MD_CONTENT = {
    'test.md': {
        'content':'# gists-test : A test md for automated testing of **GitHub Gists** critical functionality.'
    }
}
FILES_W_HTML_CONTENT = {
    'test.html': {
        'content': '<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"UTF-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n<title>Hello World Example</title>\n</head>\n<body>\n<b>Hello World</b>\n<p>Hello World</p>\n</body>\n</html>'
    }
}
FILES_W_CSS_CONTENT = {
    'test.css': {
        'content': 'test_CSS { width: 85px; height: 20px; background-image: url("http://test.test.net/hello_world.png)}'
    }
}

FILES_BY_TYPE = {
    'txt': FILES_W_TEXT_CONTENT,
    'md': FILES_W_MD_CONTENT,
    'html': FILES_W_HTML_CONTENT,
    'css': FILES_W_CSS_CONTENT,
}


TEST_GIST_IDs = ['f520cf6b2d38ede19576c48f28a53e45', '5ad0c8bcf7b2effeb2283ac0a035dea6']
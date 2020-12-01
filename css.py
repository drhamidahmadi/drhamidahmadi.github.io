for filepath in glob.iglob('./post/**/*.htm', recursive=True):
    with open(filepath) as file:
        s = file.read()
    s = s.replace('http://mihanblog.com/public/public/user_data/template/2099141/style.css', '/style.css')
    with open(filepath, "w") as file:
        file.write(s)

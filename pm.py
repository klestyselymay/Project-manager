import json
import subprocess
import os
import sys

with open('C:\Windows\System32\pm_data.json')as f:
    data = json.load(f)

with open('C:\Windows\System32\pm_data.ini')as fa:
    data_ini = fa.read()

def Create(proj_path, proj_name, proj_lang, is_pack):
    if proj_name == '':
        print('Please enter a name')
    else:
        if proj_lang == 'select language':
            print('Please select a language')
        else:
            if proj_path == '':
                print('Please enter a path')
            else:
                os.mkdir(f'{proj_path}\\{proj_name}')
                if is_pack == '-y':
                    pkg1 = {
                        "name": proj_name,
                        "version": "1.0",
                        "proj type": "Hello World",
                        "language": proj_lang
                    }
                    with open(f'{proj_path}\\{proj_name}\\package.json', 'w')as pkj:
                        json.dump(pkg1, pkj, indent=3)
                os.mkdir(f'{proj_path}\\{proj_name}\\src')
                os.mkdir(f'{proj_path}\\{proj_name}\\lib')
                os.mkdir(f'{proj_path}\\{proj_name}\\resources')
                with open(f'{proj_path}\\{proj_name}\\readme.md', 'w')as pk2:
                    pk2.write(f'#{proj_name}')

                if proj_lang == 'py':
                    with open(f'{proj_path}\\{proj_name}\\src\\main.py', 'w')as fls:
                        fls.write("""print("Hello World!")""")

                    json_str = {
                        "path": proj_path,
                        "cproj": f"{proj_path}\\{proj_name}\\src\\main.py"
                    }
                    with open(f'pm_data.json', 'w')as data_jf:
                        json.dump(json_str, data_jf, indent=3)

                
                elif proj_lang == 'rs':
                    with open(f'{proj_path}\\{proj_name}\\src\\main.rs', 'w')as fls:
                        fls.write("""fn main(){
    println!("Hello World!");
}""")               
                    json_str = {
                        "path": proj_path,
                        "cproj": f"{proj_path}\\{proj_name}\\src\\main.rs"
                    }
                    with open(f'pm_data.json', 'w')as data_jf:
                        json.dump(json_str, data_jf, indent=3)

                elif proj_lang == 'java':
                    with open(f'{proj_path}\\{proj_name}\\src\\main.java', 'w')as fls:
                        fls.write("""class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}""")               
                    json_str = {
                        "path": proj_path,
                        "cproj": f"{proj_path}\\{proj_name}\\src\\main.java"
                    }
                    with open(f'pm_data.json', 'w')as data_jf:
                        json.dump(json_str, data_jf, indent=3)

                elif proj_lang == 'c':
                    json_str = {
                        "path": proj_path,
                        "cproj": f"{proj_path}\\{proj_name}\\src\\main.c"
                    }
                    with open(f'pm_data.json', 'w')as data_jf:
                        json.dump(json_str, data_jf, indent=3)

                    with open(f'{proj_path}\\{proj_name}\\src\\main.c', 'w')as fls:
                        fls.write("""#include <stdio.h>

int main(){
    printf("Hello World!");
    return 0;
}""")

                elif proj_lang == 'cc':
                    json_str = {
                        "path": proj_path,
                        "cproj": f"{proj_path}\\{proj_name}\\src\\main.cc"
                    }
                    with open(f'pm_data.json', 'w')as data_jf:
                        json.dump(json_str, data_jf, indent=3)

                    with open(f'{proj_path}\\{proj_name}\\src\\main.cc', 'w')as fls:
                        fls.write("""#include <stdio.h>

int main(){
    printf("Hello World!");
    return 0;
}""")
                elif proj_lang == 'cs':
                    json_str = {
                        "path": proj_path,
                        "cproj": f"{proj_path}\\{proj_name}\\src\\main.cs"
                    }
                    with open(f'pm_data.json', 'w')as data_jf:
                        json.dump(json_str, data_jf, indent=3)

                    with open(f'{proj_path}\\{proj_name}\\src\\main.cs', 'w')as fls:
                        fls.write("""namespace HelloWorld
{
    class Hello {         
        static void Main(string[] args)
        {
            System.Console.WriteLine("Hello World!");
        }
    }
}""")

                elif proj_lang == 'js':
                    json_str = {
                        "path": proj_path,
                        "cproj": f"{proj_path}\\{proj_name}\\src\\main.js"
                    }
                    with open(f'pm_data.json', 'w')as data_jf:
                        json.dump(json_str, data_jf, indent=3)

                    with open(f'{proj_path}\\{proj_name}\\src\\main.js', 'w')as fls:
                        fls.write("""console.log("Hello World!");""")
                
                elif  proj_lang == 'web':
                    with open(f'{proj_path}\\{proj_name}\\index.html', 'w')as fls:
                        fls.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="style.css">
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script src="script.js"></script>
</body>
</html>""")

                    with open(f'{proj_path}\\{proj_name}\\script.js', 'w')as fls:
                        fls.write("""console.log("Hello World!");""")
                    
                    with open(f'{proj_path}\\{proj_name}\\style.css', 'w')as fls:
                        fls.write('')

                os.chdir(f'{proj_path}\\{proj_name}')
                os.system('code .')
try:
    if sys.argv[1] == '-run':
        dir1 = str(data['cproj']).split('\\')[-1]
        dir2 = str(data['cproj']).replace(f'\\{dir1}', '')
        os.chdir(dir2)
        if dir1 == 'main.py':
            nm2 = 'python'
            os.system(f"{nm2} {dir1}")
        elif dir1 == 'main.rs':
            nm2 = 'rustc'
            os.system(f"{nm2} {dir1}")
            os.system(f".{data_ini}{dir1.replace('.rs', '.exe')}")
        elif dir1 == 'main.java':
            nm2 = 'java'
            os.system(f"{nm2} {dir1}")
        elif dir1 == 'main.c':
            nm2 = 'gcc'
            os.system(f"{nm2} {dir1}")
        elif dir1 == 'main.cc':
            nm2 = 'gcc'
            os.system(f"{nm2} {dir1}")
        elif dir1 == 'main.cs':
            nm2 = 'dotnet'
            os.system(f"{nm2} {dir1}")
        elif dir1 == 'main.js':
            nm2 = 'node'
            os.system(f"{nm2} {dir1}")

    elif sys.argv[1] == '-open':
        open_proj = {"path": data['path'],"cproj": f"{data['path']}\\{sys.argv[2]}\\main.{sys.argv[3]}"}
        with open('pm_data.json', 'w')as f_f:
            json.dump(open_proj, f_f, indent=3)
        os.chdir(f"{data['path']}\\{sys.argv[2]}")
        os.system('code .')

    else:
        try:
            ab1 = sys.argv[3]
            Create(data['path'], sys.argv[1], sys.argv[2], ab1)
        except:
            Create(data['path'], sys.argv[1], sys.argv[2], 'n')
except:
    print("--commands--\n\nprojectname language - creates a project\n-run - runs the project created\n-open - opens a project")
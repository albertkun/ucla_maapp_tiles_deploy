import os, requests, json, sys, pathlib, timeit

from zipfile import ZipFile
from github import Github
from clint.textui import progress

def main(argv):
    try:
        g = Github(argv[0])
        repo = g.get_repo("albertkun/ucla_maapp_tiles_deploy")
        contents = repo.get_contents("./tiles_to_add")
        try:
            download_and_extract_tiles(contents)
        except:
            print("No new tiles, or error downloading and extracting tiles")
    except Exception as e:
        print(e)

def download_and_extract_tiles(repo_contents):
    count = 0
    home_directory = os.path.expanduser( '~' )
    for content_file in repo_contents:
        response = requests.get(content_file.url)
        response_json = json.loads(response.text)
        file_url = response_json['download_url']
        filename = pathlib.Path(file_url).stem
        outpath = f'../{pathlib.Path(file_url).stem}.zip'
        r = requests.get(file_url, stream = True)
        with open(outpath, "wb") as target_zip:
            total_length = int(r.headers.get('content-length'))
            for ch in progress.bar(r.iter_content(chunk_size = 2391975), expected_size=(total_length/1024) + 1):
                if ch:
                    target_zip.write(ch)
        with ZipFile(outpath, 'r') as zip: 
            path = os.path.join( home_directory, 'www', 'tiles',filename )
            zip.extractall(path)
        print('Deleting extracted zip file')
        os.remove(outpath) 
        count += 1
    
    print('Script complete')
    print(str(count) + ' tile(s) downloaded and extracted.')
    
if __name__ == "__main__":
   process_start = timeit.default_timer()
   main(sys.argv[1:])
   process_end = timeit.default_timer()
   print('Process took {} seconds'.format(process_end - process_start))
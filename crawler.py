import os,sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-d", "--directory", dest="directory",action="store",
                      help="name of mother directory",default="./")
parser.add_option("-e", "--execute", dest="execute",action="store_true",
                      help="set True if you want to execute",default=True)
(options, args) = parser.parse_args()
print(options)
directory_path=options.directory
execute=options.execute
#sys.exit()

#Specify path where you cloned the repository
base_dir='/u/dm/pande230/public_html/generatePlotsBase/'

def create_empty_files(directory):
    # Save current working directory
    original_directory = os.getcwd()

    try:
        # Change to the specified directory
        os.chdir(directory)
        if(not execute):
            print('Travsering following directories...')

        # For root directory
        dir_path = directory
        print(dir_path)
        cmd = "cp -r %s/* %s/"%(base_dir, dir_path)
        if(not execute):
            print(cmd)
        else:
            
            os.system(cmd)
        
        cmd = "python ./generateHtml.py"
        if(not execute):
            os.chdir(dir_path)
            print(cmd)
            os.chdir(original_directory)
        else:
            os.chdir(dir_path)
            os.system(cmd)
            os.chdir(original_directory)


        # Iterate over each sub-directory
        for root, dirs, files in os.walk(directory):
            # Iterate over sub-directories
            for dir_name in dirs:
                # Create an empty text file in each sub-directory
                #print(os.path.join(root, dir_name))
                if(dir_name == 'res'):
                    continue
                
                dir_path = os.path.join(root, dir_name)
                print(dir_path)
                cmd = "cp -r %s/* %s/"%(base_dir,dir_path)
                if(not execute):
                    print(cmd)
                else:
                    
                    os.system(cmd)
                    
                cmd = "python ./generateHtml.py"
                if(not execute):
                    os.chdir(dir_path)
                    print(cmd)
                    os.chdir(original_directory)
                else:
                    os.chdir(dir_path)
                    os.system(cmd)
                    os.chdir(original_directory)
                
                # file_path = os.path.join(root, dir_name, "empty_file.txt")
                # with open(file_path, 'w') as file:
                #     pass  # Creating an empty file

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Return to the original directory
        os.chdir(original_directory)

# Example usage:
#directory_path = "./"  # Specify the directory path here
create_empty_files(directory_path)

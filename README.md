11_duplicates
===================

The script duplicates.py takes the directory path as input. 

Then it looks through all nested directories in order to find files with the same names and sizes. 

The script outputs to console all files-duplicates. 

**Important.** Unfortunately, the script doesn't support hash comparison for now. So, if you have files with the same names and sizes, but with different content, the script will percieve them as duplicates. 

How to run
---------- 

Clone this repository. Then go to the repository directory.

Run the script:
```
python3 duplicates.py 
```

Usage
-----

```
~$ python3 duplicates.py
В какой директории будем искать дубликаты? --- ~/testfolder

Данные файлы являются дубликатами:

~/testfolder/fold3/fold7/during.txt
~/testfolder/fold3/fold4/fold5/during.txt

Данные файлы являются дубликатами:

~/testfolder/file.txt
~/testfolder/fold3/fold4/file.txt
~/testfolder/fold1/file.txt
~/testfolder/fold2/file.txt
```

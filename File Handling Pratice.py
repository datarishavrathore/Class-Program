# # # case1
# # f=open('Sample.txt','w')
# # f.write('Hello world')
# # # after close the file we didn't write any thing 
# # f.close()

# # f=open('Sample1.txt','w')
# # f.write('Python is prograamng language')
# # f.write('\nhow are you')
# # f.write('\n one day i become a Agentic AI')
# # f.close()

# # # write in a same file
# # f=open('Sample.txt','w')
# # f.write('One day')
# # f.close()

# # #if we want to add any new content without loosing previous one 
# # # use append ('a')
# # # if you want to add a new content use
# # # use ('w')

# # # We use append mode without losing previous content

# # f = open(r"C:\Users\DELL\OneDrive\Desktop\Class Program\Sample1.txt", "a")
# # f.write("\nFile handling learning")
# # f.close()


# # #
# # f=open('handle.txt','w')
# # f.write('this program i use handling')
# # f.close()

# # f=open('handle1.txt','w')
# # f.write('handling is used for handle the data without using the manual way')
# # f.close()

# # f=open('handle1.txt','w')
# # f.write('python is wideley used in data scientist files')
# # f.write('\n why we use ')
# # f.write('\nand this is good')
# # f.close()

# # f=open('handle1.txt','a')
# # f.write('this is good')
# # f.write('\nwhy we use')
# # f.close()

# # # write lines if you have list
# # l = [
# #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry.\n",
# #     "Lorem Ipsum has been the industry's standard dummy text ever since 1966.\n",
# #     "When designers at Letraset and James Mosley, the librarian at St Bride Printing Library in London.\n",
# #     "Took a 1914 Cicero translation and scrambled it to make dummy text for Letraset's Body Type sheets.\n",
# #     "It has survived not only many decades, but also the leap into electronic typesetting.\n",
# #     "Remaining essentially unchanged. It was popularised thanks to these sheets and more.\n",
# #     "Recently with desktop publishing software like Aldus PageMaker and Microsoft Word, including versions of Lorem Ipsum.\n"
# # ]

# # f = open(r"C:\Users\DELL\OneDrive\Desktop\Class Program\Sample1.txt", "a")
# # f.writelines(l)
# # f.close()


# # name=['\njim','\nMike','\n neha']
# # f=open('handle1.txt','w')
# # f.writelines(name)
# # f.close()

# # n=["It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout\n"
# # " The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English\n "
# # "Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy\n"
# # " Various versions have evolved over the years, sometimes by accident\n"
# # " sometimes on purpose (injected humour and the like\n"]

# # f=open('handle1.txt','w')
# # f.writelines(n)
# # f.close()

# # f=open('handle1.txt','r')
# # s=f.read()
# # print(s)
# # f.close()

# # f=open('Sample.txt','r')
# # s=f.read(6)
# # print(s)
# # f.close()

# # # to read limited chars you want
# # f=open('handle.txt','r')
# # s=f.read(5)
# # print(s)
# # f.close()

# # #readline-to readline by line
# # f=open('handle1.txt','r')
# # print(f.readline())
# # print(f.readline())
# # f.close()

# # #for when we don't know how many lines in the dataset
# # f=open('handle1.txt','r')
# # while True:
# #     data=f.readline()
# #     if data=='':
# #         break
# #     else:
# #         print(data)
# #     f.close()

# #     #with can be automatically close the program after the run didn't need to use f.close()
# #     with open('Sample.txt','w')as f:
# #         f.write('risahv')

# #     with open('Sample.txt','r')as f:
# #         print(f.read())

# #     with open('Sample.txt','r') as f:
# #         print(f.read())

# #     # chars after chars if we need to print
# #     with open('handle1.txt','r')as f:
# #         print(f.read(10))
# #         print(f.read(10))

# #     #for big file 
# # # Create big file using chunk
# # # big_file = ["hello world\n" for i in range(1000)]

# # # with open("rishav.txt", "w") as f:
# # #     f.writelines(big_file)

# # # # Read file
# # # with open ('rishav.txt','r')as f:
# # #     chunk_size=100

# # #     while len(f.read(chunk_size))>0:
# # #         print(f.read(chunk_size),end=' ')
# # #         f.read(chunk_size)

    
# # # chunk for larger file
# # big_L=['Ram' for i in range(1000)]

# # with open('mike.txt','w')as f:
# #     f.writelines(big_L)
    
# # with open ('mike.txt','a')as f:

# #     chunk_size=500

# # while len(f.read(chunk_size))>0:
# #     print(f.read(chunk_size),end='')
# #     f.read(chunk_size)    

# with open('sai.txt','w')as f:
#     f.write('Rishav')

# with open('Sai.txt','r')as f:
#     print(f.read())

# with open('Sai.txt','a')as f:
#     f.write('Agentic AI is good for data scientist')

# with open('Sai.txt','a')as f:
#     f.writelines('\nPython')
#     f.writelines('\nSQL')
#     f.writelines('\nPowerBI')

# with open('Sai.txt','r')as f:
#     print(f.read(3))

# with open('Sai.txt','r')as f:
#     print(f.readline())
#     print(f.readline())

# name=['Sai\n','Neha\n','Mike\n','Adam\n']
# with open('sai.txt','w')as f:
#     f.writelines(name)

# name=['this is python','and programming language', 'is a good for Data Scientist and', 'agentic ai']
# with open('Sai.txt','w')as f:
#     for i in name:
#         f.write(i+'\n')

# name=['Sai\n','Neha\n','Mike\n','Adam\n']
# with open('Sai.txt','a')as f:
#     for i in name:
#         f.writelines(i)

# pg=['Missing an EMI can negatively impact your credit score', 'making future loans harder to get!']
# with open('Sai.txt','a')as f:
#     for i in pg:
#         f.write(i)

# name=['Tanya','Sakshi']
# with open('sai.txt','w')as f:
#     f.write("\n".join(name))

# name=['Missing an EMI can negatively impact your credit score']
# with open('sai.txt','a')as f:
#     f.write("\n".join(name))

# name=['\nMissing an EMI can negatively impact your credit score']
# with open('sai.txt','a')as f:
#     for i in name:
#         f.writelines(i)
# # with open('man.txt','x')as f:
# #     f.write('Looser')

# name=['why we use','python','jin','its is a required for data scientist']
# with open('Sai.txt','w')as f:
#     f.write("\n".join(name))
        
# name=['why we use','python','ji','its is a required for data scientist']
# with open('Sai.txt','a')as f:
#     for i in name:
#         f.write(i)

# name=['why we use','python','ji','its is a required for data scientist']
# with open('sai.txt','a')as f:
#     for i in name:
#         f.write(i)

# name=['why we use','python','ji','its is a required for data scientist']
# with open('sai.txt','a')as f:
#     f.writelines("\n".join(name))

# num=['1','4','5','7']
# with open('sai.txt','a')as f:
#     f.write('\n'.join(num))

# num=['a','b','c','d']
# with open ('Sai.txt','a')as f:
#     for i in num:
#         f.write(i)

# num=['a','b','c','d']
# with open('Sai.txt','a')as f:
#     f.write("\n".join(num))

# big = ["Hello World\n" for i in range(1000)]

# with open("big.txt", "w") as f:
#     f.writelines(big)

# with open("big.txt", "r") as f:
#     chunk_size = 100

#     chunk = f.read(chunk_size)

#     while len(chunk) > 0:
#         print(chunk)
#         chunk = f.read(chunk_size)

#tell to show which next chars print

with open('Sample.txt','r')as f:
    print(f.read())
    print(f.tell())

with open('Sample.txt','r')as f:
    print(f.read())
    print(f.tell())


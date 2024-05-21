%%time
# question1 = "When did supercomputers start to develop ?"
# question1 = "How does AI work ?"
question1 = "Who built supercomputers ?"
source_file1 = 'wrong'
response1, source_file1 = obj.do_question(question=question1, language="ENGLISH")

if response1 is not None:
    get_filename_from_content = lambda file_content: (
    file_content.split('\n')[0].strip().lstrip('\\')
    )

filename = get_filename_from_content(source_file1[0].page_content)

print(" source file ", filename)
print(" response ", response1)

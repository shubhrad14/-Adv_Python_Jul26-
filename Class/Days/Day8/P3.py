# Context Manager
# Context Manager like a hotel room
# You check in (setup)
# You stay in the room (the code block)
# You check out (teardown) - automatically done
# The room is cleaned and kept ready for the next guest

# File handling
file = None
try:
    file = open('example.txt','r')
    content = file.read()
    print(content)
finally:
    if file:
        file.close()

#Multiple context managers
with open('example.txt','r') as input_file, open('output.txt','w') as output_file:
    content = input_file.read()
    output_file.write(content.upper())
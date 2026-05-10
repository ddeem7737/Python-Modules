def secure_archive(filename, action="read", content=""):

    try:
        if action == "read":
            with open(filename, "r") as file:
                data = file.read()
            return (True, data)

        elif action == "write":
            with open(filename, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")

        else:
            return (False, "Invalid action")

    except Exception as e:
        return (False, str(e))


print("=== Cyber Archives Security ===")

print("Using 'secure_archive' to read from a nonexistent file:")
print(secure_archive("/not/existing/file", "read"))

print("Using 'secure_archive' to read from an inaccessible file:")
print(secure_archive("/etc/master.passwd", "read"))

print("Using 'secure_archive' to read from a regular file:")
print(secure_archive("ancient_fragment.txt", "read"))

print("Using 'secure_archive' to write previous content to a new file:")
status, data = secure_archive("ancient_fragment.txt", "read")
if status is True:
    print(secure_archive("new_file.txt", "write", data))

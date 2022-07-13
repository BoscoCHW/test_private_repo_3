import subprocess


def main():
    process =subprocess.Popen(["git", "remote", "-v"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    output_text = output.decode("utf-8")
    print(output_text)


main()
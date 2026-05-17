Plain English: Loop through x elements, try to print each one as an integer — if it's not an integer (string, list, etc.) skip it silently. If index goes out of range, let the exception crash (don't catch IndexError).
bashcat > ~/dlh-higher_level_programming/python-exceptions/2-safe_print_list_integers.py << 'EOF'
#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count

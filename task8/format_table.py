def get_column_width(column: list) -> int:
    """Returns a length of the widest string in column."""
    return max([len(x) for x in column])


def get_all_columns_widths(benchmarks, algos, results: list) -> list:
    """Returns a list of columns width."""
    widths = list()
    widths.append(get_column_width(['Benchmark'] + benchmarks))
    for j in range(len(algos)):
        widths.append(
            get_column_width(
                [algos[j]] + [str(results[i][j]) for i in range(len(results))]))

    return widths


def print_hat(col_names: list, widths: list):
    """Prints hat string of a table."""
    hat = f'| {"Benchmark":<{widths[0]}}'
    for i in range(len(col_names)):
        hat += f' | {col_names[i]:<{widths[i + 1]}}'
    hat += ' |'

    print(hat)


def print_delim(widths: list):
    """Prints hat -> body delimiter."""
    delim = '|'
    col_num = len(widths)
    for i in range(col_num - 1):
        delim += '-' * (widths[i] + 2)
        delim += '+'
    delim += '-' * (widths[col_num - 1] + 2)
    delim += '|'

    print(delim)


def print_string(name: str, values, widths: list):
    """Prints next string of a table."""
    s = f'| {name:<{widths[0]}} |'
    for j in range(len(values)):
        s += f' {str(values[j]):<{widths[j + 1]}} |'

    print(s)


def format_table(benchmarks, algos, results: list):
    """Prints simple table of benchmarking results."""
    cols_widths = get_all_columns_widths(benchmarks, algos, results)
    print_hat(algos, cols_widths)
    print_delim(cols_widths)
    for i in range(len(benchmarks)):
        print_string(benchmarks[i], results[i], cols_widths)



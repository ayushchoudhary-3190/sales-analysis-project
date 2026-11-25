from cleaner import analyze_duplicates, anyalyze_missing_values, handle_missing_values, load_data,inspect_data, remove_duplicates, validate_data

def main():
    df = load_data()

    inspect_data(df)

    anyalyze_missing_values(df)

    df = handle_missing_values(df)

    df = analyze_duplicates(df)

    df = remove_duplicates(df)

    df = validate_data(df)

if __name__ == "__main__":
    main()
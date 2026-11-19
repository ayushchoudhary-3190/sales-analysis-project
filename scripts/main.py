from cleaner import anyalyze_missing_values, handle_missing_values, load_data,inspect_data

def main():
    df = load_data()

    inspect_data(df)

    anyalyze_missing_values(df)

    df = handle_missing_values(df)

if __name__ == "__main__":
    main()
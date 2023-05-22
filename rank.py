import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='add metadata(rank) for kiosk json file')
    
    parser.add_argument('arg1', help='kiosk json file path')
    parser.add_argument('arg2', help='output file name')

    args = parser.parse_args()
    import config_parser
    import json
    with open(args.arg1, "r", encoding="utf-8") as f:
        menu_data: dict = json.load(f)
    dis = config_parser.parse_config(args.arg1)
    for index, menu in enumerate(dis.menus):
        menu_data["items"][index]["rank"] = [i for i, _ in dis.get_rank(menu.description) if index != i ]
    with open(args.arg2,'w', encoding="utf-8") as f:
        json.dump(menu_data, f, ensure_ascii=False)
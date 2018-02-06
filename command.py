#!/usr/bin/env python3
import argparse
import search
import utils


VERSION = 'V1.0.0'
def get_parser():
    """
    解析命令行参数
    """
    parser = argparse.ArgumentParser(description='mini-torrent cli')
    parser.add_argument('-k', '--keyword', type=str,
                        help='torrent keyword.')
    parser.add_argument('-n', '--num', type=int, default=10,
                        help='magnet number.(default 50)')
    #parser.add_argument('-s', '--sort-by', type=int, default=0,
                        #help='0: Sort by date，1: Sort by size. 2: Sort by hot-rank.(default 0)')
    parser.add_argument('-o', '--output', type=str,
                        help='output file path, supports csv and json format.')
    #parser.add_argument('-p', '--pretty-oneline', action='store_true',
                        #help='show magnets info with one line.')
    parser.add_argument('-v', '--version', action='store_true',
                        help='version information.')
    return parser

def command_line_runner():
    """ 执行命令行操作
    """
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['version']:
        print(VERSION)
        return

    if not args["keyword"]:
        parser.print_help()
    else:
        magnets = search.run(kw=args["keyword"],
                      num=args["num"])
        if args["output"]:
            utils.save_file(magnets, args["output"])
        else:
            utils.print_format(magnets)

        print("搜索完成 ...")

if __name__ == '__main__':
    command_line_runner()
#!/usr/bin/env python3


def index_range(page, page_size):
    index_start = (page - 1) * page_size
    index_end = index_start + page_size - 1

    return index_start, index_end

def write_collection_doc(search_collections, file_path):
    with open(file_path, 'w+') as irg_file:
        irg_file.write('<?xml version="1.0" encoding="utf-8" standalone="no"?>\n')
        irg_file.write('<TREC>\n')
        for search_collection_id, search_collection_text in search_collections.items():
            irg_file.write('  <DOC>\n')
            irg_file.write(f'    <recordId>{search_collection_id}</recordId>\n')
            irg_file.write(f'    <text>{search_collection_text}</text>\n')
            irg_file.write('  </DOC>\n')
        irg_file.write('</TREC>\n')

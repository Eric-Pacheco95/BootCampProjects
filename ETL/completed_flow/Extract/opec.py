import datetime

from dataflows import Flow, PackageWrapper, ResourceWrapper, validate, filter_rows
from dataflows import add_metadata, dump_to_path, load, set_type, printer


def rename_resources(package: PackageWrapper):
    package.pkg.descriptor['resources'][0]['name'] = 'opec_supply_demand'
    package.pkg.descriptor['resources'][0]['path'] = 'opec_supply_demand.csv'
    package.pkg.descriptor['resources'][1]['name'] = 'opec_storage_water'
    package.pkg.descriptor['resources'][1]['path'] = 'opec_storage_water.csv'
    package.pkg.descriptor['resources'][2]['name'] = 'oil_liquid_production'
    package.pkg.descriptor['resources'][2]['path'] = 'oil_liquid_production.csv'
    package.pkg.descriptor['resources'][3]['name'] = 'glb_rig_count'
    package.pkg.descriptor['resources'][3]['path'] = 'glb_rig_count.csv'

    yield package.pkg
    res_iter = iter(package)
    for res in  res_iter:
        yield res.it
    yield from package



oil_prices = Flow(
    add_metadata(
        name="Opec_data",
        title= "A source of Opec Data",
        descriptor="A variety of temporal granularities for Europe Brent and WTI (West Texas Intermediate) Spot Prices.",
        sources=[
            {
                "name": "OPEC: Monthly Oil Market Report",
                "path": "https://www.opec.org/opec_web/static_files_project/media/downloads/publications/MOMR%20Appendix%20Tables%20(April%202020).xlsx",
                "title": "OPEC: Monthly Oil Market Report"
            },
        ]
    ),
    load(
        load_source='https://www.opec.org/opec_web/static_files_project/media/downloads/publications/MOMR%20Appendix%20Tables%20(April%202020).xlsx',
        format='xls',
        sheet=2,
        skip_rows=[1,2,3,4,5],
        headers=[' ','Country', '2016','2017','2018','1Q19','2Q19','3Q19','4Q19','2019','1Q20','2Q20','3Q20','4Q20','2020']
    ),
    load(
        load_source='https://www.opec.org/opec_web/static_files_project/media/downloads/publications/MOMR%20Appendix%20Tables%20(April%202020).xlsx',
        format='xls',
        sheet=4,
        skip_rows=[1,2,3,4,5],
        headers=[' ','_','Country','2017','2018','2019','-','Q417','1Q18','2Q18','3Q18','4Q18','1Q19','2Q19','3Q19','4Q19']
    ),
    load(
        load_source='https://www.opec.org/opec_web/static_files_project/media/downloads/publications/MOMR%20Appendix%20Tables%20(April%202020).xlsx',
        format='xls',
        sheet=5,
        skip_rows=[1,2,3,4,5,6],
        headers=[' ','Country','2016','2017','2018','3Q19','4Q19','2019','Change 19/18','1Q20','2Q20','3Q20','4Q20','Change 20/19']
    ),
    load(
        load_source='https://www.opec.org/opec_web/static_files_project/media/downloads/publications/MOMR%20Appendix%20Tables%20(April%202020).xlsx',
        format='xls',
        sheet=6,
        skip_rows=[1,2,3,4,5,6],
        headers=[' ','Country','2017','2018','2019','Change 19/18','2Q19','3Q19','4Q19','1Q20','Feb20','Mar20','Change Mar/Feb']
    ),
    rename_resources,
    validate(),
    printer(),
    dump_to_path('completed_flow/Extract/opec'),
)


oil_prices.process()


"""
This script loads data and runs the dashboard.
"""

import logging
import asyncio
from charts.main import Dashboard
from helpers.load_data import DashboardDataHandler
from streamlit_autorefresh import st_autorefresh
from shared.constants import CRONTAB_TIME
logger = logging.getLogger(__name__)
ONE_MINUTE_IN_MILISECONDS = 60000
REFRESH_TIME = ONE_MINUTE_IN_MILISECONDS * int(CRONTAB_TIME)



# async def load(dashboard):
#     dashboard_data_handler = await DashboardDataHandler.create()
#     (
#         dashboard.state,
#         dashboard.general_stats,
#         dashboard.supply_stats,
#         dashboard.collateral_stats,
#         dashboard.debt_stats,
#         dashboard.utilization_stats,
#     ) = dashboard_data_handler.load_data()

   


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    dashboard = Dashboard() # (`st.set_page_config` in `Dashboard` must be called once)
    # Set up autorefresh data config
    st_autorefresh(interval=REFRESH_TIME, key="datarefresh")

    dashboard_data_handler =  asyncio.run(DashboardDataHandler.create())
    (
        dashboard.state,
        dashboard.general_stats,
        dashboard.supply_stats,
        dashboard.collateral_stats,
        dashboard.debt_stats,
        dashboard.utilization_stats,
    ) = dashboard_data_handler.load_data()

    logger.info(f"#LOAD, state {dashboard.state}")
    logger.info(f"#LOAD, general_stats {dashboard.general_stats}")
    logger.info(f"#LOAD, supply_stats {dashboard.supply_stats}")
    logger.info(f"#LOAD, collateral_stats {dashboard.collateral_stats}")
    logger.info(f"#LOAD, debt_stats {dashboard.debt_stats}")
    logger.info(f"#LOAD, utilization_stats {dashboard.utilization_stats}")

    dashboard.run()

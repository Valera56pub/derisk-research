"""
Provides utility functions for making blockchain calls on StarkNet.
"""

import logging
import time

import starknet_py.cairo.felt
import starknet_py.hash.selector
import starknet_py.net.client_models
import starknet_py.net.networks
from starknet_py.net.full_node_client import FullNodeClient
logger = logging.getLogger(__name__)
NET = FullNodeClient(node_url="https://starknet-mainnet.public.blastapi.io")


async def func_call(addr, selector, calldata):
    """
    Executes a contract call with retry on StarkNet.
    """
    logger.info(f"FUNC_CALL {calldata}")
    print("FUNC_CALL_E")
    logger.info(selector)
    logger.info("FUNC CALL2")
    logger.info(starknet_py.hash.selector.get_selector_from_name(selector))
    call = starknet_py.net.client_models.Call(
        to_addr=addr,
        selector=starknet_py.hash.selector.get_selector_from_name(selector),
        calldata=calldata,
    )
    logger.info("FUNC CALL __A")
    # try:
    res = await NET.call_contract(call)
    #     logger.info("FUNC CALL __B")
    # except BaseException:
    #     time.sleep(10)
    #     res = await NET.call_contract(call, block_number="latest")
    #     logger.info("FUNC CALL __C")
    logger.info("FUNC CALL _XXA")
    return res


async def balance_of(token_addr, holder_addr):
    """
    Retrieves the token balance of a specified holder.
    """
    res = await func_call(
        int(token_addr, base=16), "balanceOf", [int(holder_addr, base=16)]
    )
    return res[0]


async def get_myswap_pool(id):
    """
    Fetches details of a MySwap pool by ID.
    """

    res = await func_call(
        467359278613506166151492726487752216059557962335532790304583050955123345960,
        "get_pool",
        [id],
    )

    pool_name = starknet_py.cairo.felt.decode_shortstring(res[0])  # MYSWAP ETH/USDC
    tokens = pool_name.split()[1].split("/")  # ["ETH", "USDC"]
    pool = {
        "token1": tokens[0],
        "token2": tokens[1],
        "token1_address": res[1],
        "token1_amount": res[2],
        "token2_address": res[4],
        "token2_amount": res[5],
        tokens[0]: res[2],
        tokens[1]: res[5],
    }

    return pool

from libbitcoin import bc

def satoshi_words_mainnet():
    # Create mainnet genesis block.
    block = bc.Block.genesis_mainnet()

    # Genesis block contains a single coinbase transaction.
    assert len(block.copy_transactions()) == 1

    # Get first transaction in block (coinbase).
    txs = block.copy_transactions()
    coinbase_tx = txs[0]

    # Coinbase tx has a single input.
    assert len(coinbase_tx.copy_inputs()) == 1
    coinbase_input = coinbase_tx.copy_inputs()[0]

    # Convert the input script to its raw format.
    raw_message = coinbase_input.script.to_data(False)

    # Convert to a string after removing the 8 byte checksum.
    assert len(raw_message) >= 8
    message = raw_message[8:].decode()

    assert message == "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks"

satoshi_words_mainnet()


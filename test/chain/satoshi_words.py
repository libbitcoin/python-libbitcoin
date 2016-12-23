from libbitcoin import bc

def satoshi_words_mainnet():
    # Create mainnet genesis block (contains a single coinbase transaction).
    block = bc.Block.genesis_mainnet()
    transactions = block.transactions()
    assert len(transactions) == 1

    # Coinbase tx (first in block) has a single input.
    coinbase_tx = transactions[0]
    coinbase_inputs = coinbase_tx.inputs()
    assert len(coinbase_inputs) == 1

    # Convert the input script to its raw format.
    coinbase_input = coinbase_inputs[0]
    raw_message = coinbase_input.script().to_data(False)
    assert len(raw_message) > 8

    # Convert to a string after removing the 8 byte checksum.
    message = raw_message[8:].decode()

    assert message == "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks"

satoshi_words_mainnet()


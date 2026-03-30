from cocotb.clock import Clock
import cocotb
from cocotb.triggers import RisingEdge

@cocotb.test()
async def test_sbox(dut):

    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    dut.rst_n.value = 1

    # Example input
    dut.ui_in.value = 0x53
    dut.uio_in.value = 0b10  # mode

    await RisingEdge(dut.clk)

    result = dut.uo_out.value.integer
    print(f"Output: {result:#x}")

    # Expected AES S-box output for 0x53 = 0xED
    assert result == 0xED, f"Expected 0xED, got {result:#x}"

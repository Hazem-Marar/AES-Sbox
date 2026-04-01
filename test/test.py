import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_all(dut):

    for i in range(10):
        dut.ui_in.value = i
        dut.uio_in.value = i + 1

        await Timer(10, units="ns")

        print(f"A={i}, B={i+1}, OUT={dut.uo_out.value}")

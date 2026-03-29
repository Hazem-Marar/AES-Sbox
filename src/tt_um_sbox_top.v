module tt_um_sbox_top (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       clk,
    input  wire       rst_n
);

    wire [7:0] data_o;
    wire [1:0] mode;

    // Map inputs
    assign mode = uio_in[1:0];

    // No bidirectional outputs used
    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

    // Your original logic (unchanged behavior)
    sbox_top_internal core (
        .clk(clk),
        .rst_n(rst_n),
        .mode(mode),
        .data_i(ui_in),
        .data_o(data_o)
    );

    assign uo_out = data_o;

endmodule
designed by bingSanDianShui
example 1:	uart_tx_top ( Clk, Rst_n, Rs232_Tx, key_in0, led );
example 2:	
		uart_byte_tx(
			Clk,
			Rst_n,
			data_byte,
			send_en,
			baud_set,
			Rs232_Tx,
			Tx_Done,
			uart_state
			);

end
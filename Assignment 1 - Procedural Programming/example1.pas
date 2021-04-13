program AskName(input, output);
var
	response: string;
begin
    writeLn('What is your name? ');
	
	readLn(input, response);
	writeLn('hello ', response, '!')
end.
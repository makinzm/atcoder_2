n = gets.to_i
w = gets.split

w_dict = {
    'b' => 1,
    'c' => 1,
    'd' => 2,
    'w' => 2,
}
w_dict['t'] = 3
w_dict['j'] = 3
w_dict['f'] = 4
w_dict['q'] = 4
w_dict['l'] = 5
w_dict['v'] = 5
w_dict['s'] = 6
w_dict['x'] = 6
w_dict['p'] = 7
w_dict['m'] = 7
w_dict['h'] = 8
w_dict['k'] = 8
w_dict['n'] = 9
w_dict['g'] = 9
w_dict['z'] = 0
w_dict['r'] = 0


w.each do |word|
    word.downcase!
    word.split('').each do |c|
        if w_dict.has_key?(c)
            word.gsub!(c,w_dict[c].to_s)
        else
            word.gsub!(c,'')
        end
    end
end

puts w.select{|word| word.length != 0}.join(' ')

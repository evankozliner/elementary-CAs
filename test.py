import png

def next_row(row, rule_bits):
    r = row[-1:] + row + row[:1]
    return [rule_bits[r[i]*4 + b*2 + r[i+2]] for (i, b) in enumerate(row)]

def save_png_data(rows, filename):
    ll = [[255 - b * 255 for b in row] for row in rows]
    png.from_array(ll, 'L').save(filename)

def run():

    rule = 110 # or 0b01101110

    (WIDTH, HEIGHT) = (2500, 2500)

    row = [0] * (WIDTH-1) + [1]

    s = bin(rule)[2:].zfill(8)
    rule_bits = [int(x) for x in s[::-1]]

    png_data = [row]

    for i in range(HEIGHT):
        row = next_row(row, rule_bits)
        png_data.append(row)

    save_png_data(png_data, "rule_%d_%d_%s.png" % (rule, WIDTH, HEIGHT))

if __name__ == "__main__":
    run()

import os
import csv


for (__, dirlist, _) in os.walk('./'):
    for dir in dirlist:
        target = dir;
        #target = 'SM6_TITANX';
        with open(target+'_record.csv', 'w', newline='') as exp_f:
            # parse the exp result and write in .csv file.
            writer = csv.writer(exp_f)
            writer.writerow([target, "simulation_time", "simulation_rate (inst/sec)", "simulation_rate(cycle/sec)", "silicon_slowdown"])
            record_array = []
            for filename in os.listdir(target):
                with open(os.path.join(target, filename), 'r') as f:
                    filename = filename[:filename.find('_SM')].lower() + filename[filename.find('output_')+6:filename.find('.txt')]
                    lines = f.readlines()
                    for i in range(10000000):
                        if 'gpgpu_silicon_slowdown' in lines[-i]:
                            lines[-i-3] = lines[-i-3].strip('\n')  # gpgpu_sim_time
                            lines[-i-3] = lines[-i-3][lines[-i-3].find('(')+1:-5]
                            lines[-i-2] = lines[-i-2].strip('\n')
                            lines[-i-2] = lines[-i-2][24:lines[-i-2].find('(') - 1]
                            lines[-i-1] = lines[-i-1].strip('\n')
                            lines[-i-1] = lines[-i-1][24:lines[-i-1].find('(') - 1]
                            lines[-i] = lines[-i].strip('\n')
                            lines[-i] = lines[-i][25:lines[-i].find('x')]
                            list_rows = [filename, lines[-i-3], lines[-i-2], lines[-i-1], lines[-i]]
                            record_array.append(list_rows)
                            break
            # sort .csv file by lexicographic order
            record_array.sort()
            for row in record_array:
                writer.writerow(row)

            print(record_array)
            print()


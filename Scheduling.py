from IPython.display import clear_output as cls

class Scheduling:

    def __init__(self):
        self.process = []
        self.first = None
        self.last = None
        self.num_node = 0

    def Selection(self):
        choice = int(input('1) First Come First Serve\n'+
                           '2) Shortest Job First\n' +
                           '3) Shortest Remaining Time First\n' +
                           '4) Priority Scheduling\n'+
                           '5) Round Robin\n Choice:  '))

        if choice == 1:
            cls()
            print('First Come First Serve')
            j = int(input('Input number of Processes: '))
            for i in range(j):
                print('Process {}'.format(i+1))
                burst = int(input('\t Input Burst Time: '))
                self.FCFS_process(i, burst)
            self.FCFS_scheduling()
        elif choice == 2:
            cls()
            print('Shortest Job First')
            j = int(input('Input number of Processes: '))
            for i in range(j):
                print('Process {}'.format(i+1))
                burst = int(input('\t Input Burst Time: '))
                self.SJF_process(i, burst)
            self.SJF_scheduling()
        elif choice == 3:
            cls()
            print('Shortest Remaining Time First')
            j = int(input('Input number of Processes: '))
            for i in range(j):
                print('Process {}'.format(i+1))
                arrival = int(input('\t Input Arrival Time:'))
                burst = int(input('\t Input Burst Time: '))
                self.SRTF_process(i,arrival, burst)
            self.SRTF_scheduling()
        elif choice == 4:
            cls()
            print('Priority Scheduling')
            j = int(input('Input number of Processes: '))
            for i in range(j):
                print('Process {}'.format(i+1))
                burst = int(input('\t Input Burst Time: '))
                priority = int(input('\t Input Priority Number: '))
                self.P_process(i,priority, burst)
            self.P_scheduling()
        else:
            cls()
            print('Round Robin')
            j = int(input('Input number of Processes: '))
            for i in range(j):
                print('Process {}'.format(i+1))
                burst = int(input('\t Input Burst Time: '))
                self.RR_process(i, burst)
            y = int(input('Time: '))
            self.RR_scheduling()

    def FCFS_process(self,number,burst):
        self.process.append([number, burst])

    def FCFS_scheduling(self):
        lst=[]
        time=0
        log={}

        for i in self.process:
            log[time] = i[0]
            time += i[1]
        log[time]=None
        self.FCFS_draw(log)

    def FCFS_draw(self, log):
        j = 0
        print('Gantt Chart:')
        for i in log:
            j += i if log.get(i) is not None else 0
            print('|{}|\t{}\t'.format(i,('P' + str(log.get(i) + 1)) if log.get(i) is not None else None  ), end="")
        print('\n\nAverage waiting time: {}'.format(j/len(self.process)))

    def SJF_process(self,number,burst):
        self.process.append([number,burst])

    def SJF_scheduling(self):
        lst=[]
        time=0
        log={}
        for i in self.process:
            lst.append(i[1])
        while(lst):
            log[time]=lst.index(min(lst))
            time += min(lst)
            lst.remove(min(lst))
        log[time]=None
        self.SJF_draw(log)

    def SJF_draw(self, log):
        j = 0
        print('Gantt Chart:')
        for i in log:
            j += i if log.get(i) is not None else 0
            print('|{}|\t{}\t'.format(i,('P' + str(log.get(i) + 1)) if log.get(i) is not None else None  ), end="")
        print('\n\nAverage waiting time: {}'.format(j/len(self.process)))

    def SRTF_process(self,number,arrival, burst):
        self.process.append([number,arrival,burst])

    def SRTF_scheduling(self):
        process = []
        lst = []
        for i in self.process:
            process.append(i)
            lst.append(i[2])
        complete = 0
        WT = [0]*len(process)
        track= [0]*len(process)
        accom = 0
        time = 0
        counter = 0
        log = {}
        switch = False

        while complete < len(process):
            for i in range(len(process)):
                if process[i][1] == time:
                    if accom is None:
                        accom = i
                        WT[accom] = time
                    elif process[accom][2] > process[i][2]:
                        counter = 0
                        accom = i
                        WT[accom] = time
            if switch:
                for i in range(len(process)):
                    if process[i][1] < time:
                        if process[accom][2] == 0 and process[i][2] > 0:
                            accom = i
                            WT[accom] = time
                        elif process[i][2] > 0 and process[accom][2] > process[i][2]:
                            accom = i
                            WT[accom] = time
                counter = 0
                switch = False
            log[time] = 'P'+ str(accom+1)
            process[accom][2] -= 1
            counter += 1
            time += 1

            if process[accom][2] == 0:
                complete += 1
                track[accom] = WT[accom] - process[accom][1]
                if counter != lst[accom]:
                    track[accom] = track[accom] - (lst[accom] - counter)
                counter = 0
                switch = True

        log[time] = None
        self.SRTF_draw(log,time, sum(track)/len(process))

    def SRTF_draw(self, log):
        process = log[0]
        print('Gantt Chart:')
        print('|{}|\t{}\t'.format(0, log[0]), end = "")
        for i in range(time+1):
            if log[i] != process:
                process = log[i]
                print('|{}|\t{}\t'.format(i, log[i] if log[i] is not None else None), end = "")
        print('\n\nAverage Waiting Time: {}'.format(avg))

    def P_process(self,number,priority, burst):
        self.process.append([number,priority,burst])

    def P_scheduling(self):
        zxc = []
        time = 0
        log = {}
        accom_time = []
        for i in self.process:
            zxc.append(i[1])

        while zxc:
            no = min(zxc)
            for i in self.process:
                if no == i[1]:
                    self.deqwe(i[0])

            zxc.remove(min(zxc))


        while self.head() is not None:
            prio = self.head().getValue()
            count = 0
            for i in self.process:
                if i[0] == prio:
                    break
                count += 1

            accom_time.append(time)

            while self.process[count][2] != 0:
                log[time] = self.process[count][0]
                self.process[count][2] -= 1
                time += 1


            self.deqwe()

        log[time] = None
        self.P_draw(log,time,sum(accom_time)/len(self.process))

    def P_draw(self, log, time, avg):
        process = log[0]
        print('Gantt Chart: ')
        print('|{}|\t{}\t'.format(0, log[0]), end = "")
        for i in range(time+1):
            if log[i] != process:
                process = log[i]
                print('|{}|\t{}\t'.format(i, ('P' + str(log.get(i) + 1)) if log.get(i) is not None else None ), end = "")
        print('\n\nAverage Waiting Time: {}'.format(avg))

    def RR_process(self,number,burst):
        self.process.append([number,burst])

    def RR_scheduling(self, time_quantom):
        count = 0
        log = {}
        time = 0
        burst_time = 0
        accom_time = 0;
        for i in self.proc:
            burst_time += i[1]

        while burst_time != 0:
            while count < time_quantom and self.proc[accom_time][1] != 0:
                log[time] = self.proc[accom_time][0]
                self.proc[accom_time][1] -= 1
                time += 1
                count += 1
            accom_time += 1
            count = 0
            burst_time = 0
            for i in self.proc:
                burst_time += i[1]
            if accom_time > len(self.proc)-1:
                accom_time = 0

        log[time] = None
        self.RR_draw(log,time,time_quantom)

    def RR_draw(self,log,time,tQ):
        process = log[0]
        count = 0
        print('Gantt Chart:')
        print('|{}|\t{}\t'.format(0, 'P'+str(log[0])), end = "")
        for i in range(time+1):
            if count == tQ or log[i] != process:
                count = 0
                if log[i] != process:
                    process = log[i]
                    print('|{}|\t{}\t'.format(i, ('P' + str(log.get(i))) if log.get(i) is not None else None ), end = "")
                else:
                    print('|{}|\t{}\t'.format(i, ('P' + str(log.get(i))) if log.get(i) is not None else None ), end = "")
            count += 1

    def enqwe(self,value):
        node = Node(value)
        if (self.num_node == 0):
            self.first = node
            self.last = node
            self.num_node += 1
        else:
            node.set_nxt(self.last)
            self.last.set_prev(node)
            self.last = node
            self.num_node +=1

    def deqwe(self,value):
        if (self.num_node != 0):
            self.temp_node = self.first.get_prev()
            self.first = self.temp_node

    def tail(self):
        return self.last

    def head(self):
        return self.first

class Node:
    def __init__(self, value):
        self.value = value
        self.nxt = None
        self.prev = None

    def get_nxt(self):
        return self.nxt

    def get_prev(self):
        return self.prev

    def set_nxt(self,nxt):
        self.nxt = nxt

    def set_prev(self, prev):
        self.prev = prev

    def get_value(self):
        return self.value

a = Scheduling()
a.Selection()

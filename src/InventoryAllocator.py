class InventoryAllocator:
    match = 'no'
    def calculate_cheapest_shipment(self, input1, input2):
        """
        Function produces and returns the cheapest shipment
        :param input1: It is the input containing the required orders
        :param input2: It consists of warehouses and its respective inventories
        :return: Returns output list containing the matched warehouses
        """
        output_list1 = []
        dict1 = []
        self.match = 'no'
        if (len(input1)) > 0:  # Checking if there are orders i.e, input1 is not {}
            for i in input1:
                if input1[i] == 0:  # Checking if the orders are empty. For example, {"apple" : 0 }
                    return "No allocation"
                else:
                    output_list = self.perf_check(i, input1, input2, output_list1)
                    if output_list:
                        output_list1.append(output_list)
                    else:
                        diff = input1[i]
                        for j in range(0, len(input2)):
                            if i in input2[j]['inventory']:  # Checking if the order is present in inventory
                                if input1[i] >= input2[j]['inventory'][i] != 0:
                                    diff = diff - input2[j]['inventory'][i]
                                    if diff > 0:
                                        output = "{ " + str(input2[j]['name']) + " : " + "{ " + i + " : " + str(
                                            input2[j]['inventory'][i]) + " }}"
                                        dict1.append(output)
                                    elif diff <= 0:
                                        output = "{ " + str(input2[j]['name']) + " : " + "{ " + i + " : " + str(
                                            input2[j]['inventory'][i]) + " }}"
                                        dict1.append(output)
                                        self.match = 'yes'
                                        output_list1.append(dict1)
                                        break
        if self.match == 'no':
            return "No allocation"
        else:
            return output_list1

    def perf_check(self, i, input1, input2, output_list1):
        """
        Function checks if the match is perfect, without the need to split the order across warehouses.
        :param i: order. For example: apple
        :param input1: It is the input containing the required orders
        :param input2: It consists of warehouses and its respective inventories
        :param output_list1: Contains the attributes of warehouses which are matched
        :return: It returns the output list and match variable
        """
        output = []
        for j in range(0, len(input2)):
            if i in input2[j]['inventory']:  # Checking if the order is present in inventory

                if input1[i] == input2[j]['inventory'][i] or input1[i] <= input2[j]['inventory'][i]:
                    self.match = 'yes'
                    output = "{ " + str(input2[j]['name']) + " : " + "{ " + i + " : " + str(
                        input2[j]['inventory'][i]) + " }}"
                    break
        return output


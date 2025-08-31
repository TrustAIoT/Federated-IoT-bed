class Math:
    @staticmethod
    def clamp(value, min, max):
        if value < min:
            return min
        elif value > max:
            return max
        else:
            return value
    
    @staticmethod
    def convertRange(value, oldMin, oldMax, newMin, newMax):
        return (value - oldMin) / (oldMax - oldMin) * (newMax - newMin) + newMin
    
    @staticmethod
    def clampFloatToInt(value, minFloat, maxFloat, minInt, maxInt):
        intValue = int((value - minFloat) / (maxFloat - minFloat) * (maxInt - minInt) + minInt)
        return Math.clamp(intValue, minInt, maxInt)
    
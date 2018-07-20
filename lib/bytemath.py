# -*- coding: utf-8 -*-

def Kib_to_b(kbs_number):
	return int(kbs_number * 1024)
def Mib_to_b(mbs_number):
	return Kib_to_b(mbs_number * 1024)
def Gib_to_b(gbs_number):
	return Mib_to_b(gbs_number * 1024)
def Tib_to_b(tbs_number):
	return Gib_to_b(tbs_number * 1024)
def Pib_to_b(pbs_number):
	return Tib_to_b(pbs_number * 1024)
def Eib_to_b(ebs_number):
	return Pib_to_b(ebs_number * 1024)

def unit_to_bytes(size,unit):
	if(unit == "Kb"):
		return Kib_to_b(size)
	elif(unit == "Mb"):
		return Mib_to_b(size)
	elif(unit == "Gb"):
		return Gib_to_b(size)
	elif(unit == "Tb"):
		return Tib_to_b(size)
	elif(unit == "Pb"):
		return Pib_to_b(size)
	elif(unit == "Eb"):
		return Eib_to_b(size)
# -*- coding: utf-8 -*-
"""mpi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M37JV705iWAjZ3es880b9-KhdOwn-Fa3
"""

from mpi4py import MPI


class MPI_klasa(object):

   
    def bcast(data):
        if MPI_INSTALLED:
            mpi_comm = MPI.COMM_WORLD
            bdata = mpi_comm.bcast(data, root=0)
        else:
            bdata = data
        return bdata

    
    def barrier(self):
        if MPI_INSTALLED:
            mpi_comm = MPI.COMM_WORLD
            mpi_comm.barrier()

    
    def rank(self):
        if MPI_INSTALLED:
            mpi_comm = MPI.COMM_WORLD
            return mpi_comm.Get_rank()
        else:
            return 0

 
    def size(self):
        if MPI_INSTALLED:
            mpi_comm = MPI.COMM_WORLD
            return mpi_comm.Get_size()
        else:
            return 1
    

    def is_master(self):
       
        return self.rank == 0

  
    def split_seq(self, sequence):
        
        starts = [i for i in range(0, len(sequence), len(sequence)//self.size)]
        ends = starts[1: ] + [len(sequence)]
        start, end = list(zip(starts, ends))[self.rank]

        return sequence[start: end]

    def split_size(self, size):
       
        if size < self.size:
            warn_msg = ('Splitting size({}) je manja od procesa ' 
                       
            self._logger.warning(warn_msg)
            splited_sizes = [1]*size + [0]*(self.size - size)
        elif size % self.size != 0:
            residual = size % self.size
            splited_sizes = [size // self.size]*self.size
            for i in range(residual):
                splited_sizes[i] += 1
        else:
            splited_sizes = [size // self.size]*self.size

        return splited_sizes[self.rank]

    def merge_seq(self, seq):
       
        if self.size == 1:
            return seq
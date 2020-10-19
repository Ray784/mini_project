# mini-project


ds-141-3   --->  (syllable n-gramming not applied)Folder consisting of 141 telugu documents with three categores
ds-t2-141-3 ---> (syllable 2-gram applied)Folder consisting of 141 telugu documents with three categories where each word is of atmost length 2.
ds-t3-141-3 ---> (syllable 3-gram applied)Folder consisting of 141 telugu documents with three categories where each word is of atmost length 3.
ds-t4-141-3 ---> (syllable 4-gram applied)Folder consisting of 141 telugu documents with three cateogories where each word is of atmost length 4.

outputs-ds-141  ----> Folder consisting of time taken and measurements of outcomes when pca,kpca is applied to 141 telugu documents with no syllable n gramming.
                      output.txt --> This file contains efficiency calculated after applying clustering and pca,kpca on different dimensions.
                      time_opt.txt--> This file contains time taken by clustering and pca,kpca with difference dimensions
outputs-ds-t2-141  ----> Folder consisting of time taken and measurements of outcomes when pca,kpca is applied to 141 telugu documents with 2-syllable gramming.
                      output.txt --> This file contains efficiency calculated after applying clustering and pca,kpca on different dimensions.
                      time_opt.txt--> This file contains time taken by clustering and pca,kpca with difference dimensions
                  
outputs-ds-t3-141  ----> Folder consisting of time taken and measurements of outcomes when pca,kpca is applied to 141 telugu documents with 3-syllable gramming.
                      output.txt --> This file contains efficiency calculated after applying clustering and pca,kpca on different dimensions.
                      time_opt.txt--> This file contains time taken by clustering and pca,kpca with difference dimensions
 
outputs-ds-t4-141  ----> Folder consisting of time taken and measurements of outcomes when pca,kpca is applied to 141 telugu documents with 4-syllable gramming.
                      output.txt --> This file contains efficiency calculated after applying clustering and pca,kpca on different dimensions.
                      time_opt.txt--> This file contains time taken by clustering and pca,kpca with difference dimensions.
 
components -->    Go to pca-ds-141-3/pca-mindf-0.02 Folder.

nlp-new-build.py --> Program to apply pca(dimension reduction) and clustering on input documents.

/*
   Copyright (c) 2009-2014, Jack Poulson
   All rights reserved.

   This file is part of Elemental and is under the BSD 2-Clause License, 
   which can be found in the LICENSE file in the root directory, or at 
   http://opensource.org/licenses/BSD-2-Clause
*/
#pragma once
#ifndef ELEM_BLOCKDISTMATRIX_MR_STAR_DECL_HPP
#define ELEM_BLOCKDISTMATRIX_MR_STAR_DECL_HPP

namespace elem {

// Partial specialization to A[MR,* ].
//
// The rows of these distributed matrices will be replicated on all 
// processes (*), and the columns will be distributed like "Matrix Rows" 
// (MR). Thus the columns will be distributed among rows of the process
// grid.
template<typename T>
class BlockDistMatrix<T,MR,STAR> : public GeneralBlockDistMatrix<T,MR,STAR>
{
public:
    // Typedefs
    // ========
    typedef AbstractBlockDistMatrix<T> absType;
    typedef GeneralBlockDistMatrix<T,MR,STAR> genType;
    typedef BlockDistMatrix<T,MR,STAR> type;

    // Constructors and destructors
    // ============================

    // Inherited constructors are part of C++11 but not yet widely supported.
    //using GeneralDistMatrix<T,MR,STAR>::GeneralDistMatrix;

    // Create a 0 x 0 distributed matrix
    BlockDistMatrix
    ( const elem::Grid& g=DefaultGrid(), Int blockHeight=32, Int blockWidth=32,
      Int root=0 );
    // Create a height x width distributed matrix
    BlockDistMatrix
    ( Int height, Int width, const elem::Grid& g=DefaultGrid(),
      Int blockHeight=32, Int blockWidth=32, Int root=0 );
    // Create a height x width distributed matrix with specified alignments
    BlockDistMatrix
    ( Int height, Int width, const elem::Grid& g,
      Int blockHeight, Int blockWidth,
      Int colAlign, Int rowAlign, Int colCut, Int rowCut,
      Int root=0 );
    // Create a height x width distributed matrix with specified alignments
    // and leading dimension
    BlockDistMatrix
    ( Int height, Int width, const elem::Grid& g,
      Int blockHeight, Int blockWidth,
      Int colAlign, Int rowAlign, Int colCut, Int rowCut, Int ldim,
      Int root=0 );
#ifndef SWIG
    // View a constant distributed matrix's buffer
    BlockDistMatrix
    ( Int height, Int width, const elem::Grid& g,
      Int blockHeight, Int blockWidth,
      Int colAlign, Int rowAlign, Int colCut, Int rowCut,
      const T* buffer, Int ldim, Int root=0 );
#endif
    // View a mutable distributed matrix's buffer
    BlockDistMatrix
    ( Int height, Int width, const elem::Grid& g,
      Int blockHeight, Int blockWidth,
      Int colAlign, Int rowAlign, Int colCut, Int rowCut,
      T* buffer, Int ldim, Int root=0 );

    // Create a copy of distributed matrix A (redistributing if necessary)
    BlockDistMatrix( const type& A );
    template<Dist U,Dist V> BlockDistMatrix( const BlockDistMatrix<T,U,V>& A );
    template<Dist U,Dist V> BlockDistMatrix( const DistMatrix<T,U,V>& A );
#ifndef SWIG
    // Move constructor
    BlockDistMatrix( type&& A ) noexcept;
#endif
    // Destructor
    ~BlockDistMatrix();

    // Assignment and reconfiguration
    // ==============================
    template<Dist U,Dist V> type& operator=( const DistMatrix<T,U,V>& A );
    type& operator=( const BlockDistMatrix<T,MC,  MR  >& A );
    type& operator=( const BlockDistMatrix<T,MC,  STAR>& A );
    type& operator=( const BlockDistMatrix<T,STAR,MR  >& A );
    type& operator=( const BlockDistMatrix<T,MD,  STAR>& A );
    type& operator=( const BlockDistMatrix<T,STAR,MD  >& A );
    type& operator=( const BlockDistMatrix<T,MR,  MC  >& A );
    type& operator=( const BlockDistMatrix<T,MR,  STAR>& A );
    type& operator=( const BlockDistMatrix<T,STAR,MC  >& A );
    type& operator=( const BlockDistMatrix<T,VC,  STAR>& A );
    type& operator=( const BlockDistMatrix<T,STAR,VC  >& A );
    type& operator=( const BlockDistMatrix<T,VR,  STAR>& A );
    type& operator=( const BlockDistMatrix<T,STAR,VR  >& A );
    type& operator=( const BlockDistMatrix<T,STAR,STAR>& A );
    type& operator=( const BlockDistMatrix<T,CIRC,CIRC>& A );
 #ifndef SWIG
    // Move assignment
    type& operator=( type&& A );
#endif

    // Realignment
    // -----------
    virtual void AlignWith( const elem::BlockDistData& data );
    virtual void AlignColsWith( const elem::BlockDistData& data );

    // Basic queries
    // =============
    virtual elem::BlockDistData DistData() const;
    virtual mpi::Comm DistComm() const;
    virtual mpi::Comm CrossComm() const;
    virtual mpi::Comm RedundantComm() const;
    virtual mpi::Comm ColComm() const;
    virtual mpi::Comm RowComm() const;
    virtual Int ColStride() const;
    virtual Int RowStride() const;

private:
    // Friend declarations
    // ===================
#ifndef SWIG
    template<typename S,Dist U,Dist V> friend class DistMatrix;
    template<typename S,Dist U,Dist V> friend class BlockDistMatrix;
#endif 
};

} // namespace elem

#endif // ifndef ELEM_BLOCKDISTMATRIX_MR_STAR_DECL_HPP
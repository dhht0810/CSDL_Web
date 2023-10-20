package com.example.thu_vien.dao;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.example.thu_vien.entities.Truyen;

@Repository
public interface TruyenRepository extends CrudRepository<Truyen,Integer> {

    List<Truyen> findByTenContainingOrTacgiaContaining(String ten, String tacgia);

}

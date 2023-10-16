package com.example.thu_vien.dao;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.example.thu_vien.entities.The_loai;

@Repository
public interface The_loaiRepository extends CrudRepository<The_loai,Integer> {
    
}

package com.example.thu_vien.dao;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.example.thu_vien.entities.Chap;
import java.util.List;


@Repository
public interface ChapRepository extends JpaRepository<Chap, Integer> {
    List<Chap> findByIdtrIs(int id_truyen);
}

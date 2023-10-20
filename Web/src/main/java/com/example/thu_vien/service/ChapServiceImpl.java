package com.example.thu_vien.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.thu_vien.dao.ChapRepository;
import com.example.thu_vien.entities.Chap;

@Service
public class ChapServiceImpl implements ChapService {
    @Autowired
    private ChapRepository chapRepository;

    @Override
    public void save(Chap chap) {
        chapRepository.save(chap);
    }

    @Override
    public void delete(Integer id) {
        chapRepository.deleteById(id);
    }

    @Override
    public List<Chap> findById_truyen(int id_truyen) {
        return chapRepository.findByIdtrIs(id_truyen);
    }
    
}

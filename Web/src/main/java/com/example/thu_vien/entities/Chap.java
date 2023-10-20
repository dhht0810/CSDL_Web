package com.example.thu_vien.entities;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Table(name = "chap")
@Getter
@Setter
@NoArgsConstructor
public class Chap {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    @Column(insertable=false, updatable=false)
    private int idtr;
    private String filePath;
    private int id_chap;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "idtr")
    private Truyen truyen;

    public Chap(int idtr) {
        this.idtr = idtr;
    }

    @Override
    public int hashCode() {
        final int prime = Integer.MAX_VALUE;
        int result = 1;
        result = prime * result + ((id == null) ? 0 : id.hashCode());
        return result;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Chap other = (Chap) obj;
        if (id == null) {
            if (other.id != null)
                return false;
        } else if (!id.equals(other.id))
            return false;
        return true;
    }
}

